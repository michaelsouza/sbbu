import os
import subprocess
import pandas as pd

from rich.console import Console
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)
from rich.table import Table
from rich.traceback import install as rich_traceback_install

rich_traceback_install(show_locals=False)
console = Console()


def run_cmd(cmd):
    verbose = os.environ.get("SBBU_VERBOSE", "").lower() in {"1", "true", "yes", "y"}
    output = [cmd + '\n']
    console.print(f"[dim]$ {cmd}[/dim]")
    try:
        if os.name == 'nt':  # windows
            cmd_out = subprocess.check_output(cmd, shell=True).decode('windows-1252')
        else:  # unix
            cmd_out = subprocess.check_output(cmd, shell=True).decode('utf-8')
        cmd_out = cmd_out.split('\n')
        for line in cmd_out:
            if verbose:
                console.print(line)
            output.append(line + '\n')
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Command failed[/red]: {e}")
        if getattr(e, "output", None):
            try:
                out = e.output.decode("utf-8", errors="replace").splitlines()
                for line in out:
                    if verbose:
                        console.print(line)
                    output.append(line + "\n")
            except Exception:
                pass
    return output


def create_table(flog):
    with open(flog, 'r') as fid:
        data = fid.readlines()

    df = {'pid': [], 'nnodes': [], 'nedges': [], 'tsec': [], 'mde': [], 'lde': []}
    for row in data:
        if 'Reading file' in row:
            pid = row.split('/')[-1].split('.')[0]
            for col in df:
                df[col].append(None)
            df['pid'][-1] = pid
        if 'NMR: nnodes' in row:
            df['nnodes'][-1] = int(row.split()[-1])
        if 'NMR: nedges' in row:
            # edges (i, j) and (j, i) are included (duplicated)
            df['nedges'][-1] = int(int(row.split()[-1]) / 2)
        if 'MDE' in row and 'LDE' in row:
            df['mde'][-1] = float(row.split()[3].replace(',', ''))
            df['lde'][-1] = float(row.split()[-1])
        if 'solution found after' in row:
            df['tsec'][-1] = float(row.split()[-2])

    df = pd.DataFrame.from_dict(df)
    ftab = flog.replace('.log', '.csv')
    console.print(f"\n[bold]TABLE[/bold] {ftab}")
    table = Table(show_header=True, header_style="bold")
    for col in df.columns:
        table.add_column(str(col))
    for _, row in df.iterrows():
        table.add_row(*[("" if pd.isna(v) else str(v)) for v in row.tolist()])
    console.print(table)
    df.to_csv(ftab)

if __name__ == "__main__":
    tmax = 300
    WDIR = ['DATA_EPSD_00_DMAX_50', 'DATA_EPSD_00_DMAX_60']
    solver = 'sbbu.exe' if os.name == 'nt' else './sbbu.exe'
    for wdir in WDIR:
        console.rule(f"[bold]{wdir}[/bold]")
        FILES = []
        for fname in os.listdir(wdir):
            fname = os.path.join(wdir, fname)
            if fname.endswith('.nmr'):
                FILES.append({'name': fname, 'size': os.path.getsize(fname)})
        FILES = sorted(FILES, key=lambda x: x['size'])

        output = []
        progress = Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("{task.completed}/{task.total}"),
            TimeElapsedColumn(),
            TimeRemainingColumn(),
            console=console,
        )
        with progress:
            task_id = progress.add_task("Running", total=len(FILES))
            for k, f in enumerate(FILES, start=1):
                progress.update(
                    task_id,
                    description=f"[{k}/{len(FILES)}] {f['size']} : {f['name']}",
                )
                cmd = '%s -nmr %s -tmax %f' % (solver, f['name'], tmax)
                output += run_cmd(cmd)
                progress.advance(task_id, 1)

        # create log file
        flog = wdir + '.log'
        console.print(f"[dim]saving file {flog}[/dim]")
        with open(flog, 'w') as fid:
            for row in output:
                fid.write(row)

        # create table of results
        create_table(wdir + '.log')
