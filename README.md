# SBBU
SBBU is an algorithm to Discretizable Molecular Distance Geometry Problems.

# Compilation
To compile sbbu, just type

~~~
make sbbu.exe
~~~

# Execution
In order to execute is necessary to specify the NRM file (-nmr) and the max execution time (-tmax).

Example:
~~~
./sbbu.exe -nmr DATA_EPSD_00_DMAX_50/1n6t.nmr -tmax 10
~~~

# Test installation
The installation can be checked by typing

~~~
make test_all
~~~

# Reference results
The folder "REFERENCE RESULTS" contains the results obtained on Intel Core i7-8750H (Linux Ubuntu WSL).

TABLE DATA_EPSD_00_DMAX_50.csv ==============================
     pid  nnodes  nedges      tsec           mde           lde
  0   1n6t      30     176  0.000132  5.644470e-12  3.527690e-10
  1   1fw5      60     417  0.000347  2.475890e-12  1.055050e-10
  2   1adx     120     659  0.000476  2.925420e-12  5.903880e-10
  3   1bdo     241    1345  0.000959  8.486120e-12  6.954290e-10
  4   1all     480    3443  0.002937  1.234330e-12  2.982270e-09
  5   6s61     522    3699  0.002850  2.962390e-12  1.338150e-09
  6   1fhl    1002    6378  0.004533  1.021050e-11  3.983290e-09
  7   4wua    1033    6506  0.004682  2.912080e-12  1.030460e-09
  8   6czf    1494    9223  0.006373  2.351170e-12  1.185490e-09
  9   5ijn    1950   11981  0.008298  7.242990e-12  4.478620e-09
  10  6rn2    2052   13710  0.010145  6.215990e-12  2.638640e-09
  11  1cza    2694   17451  0.012554  3.219920e-11  1.966340e-08
  12  6bco    2856   18604  0.013475  8.945790e-12  2.501330e-08
  13  1epw    3861   23191  0.015696  9.522180e-11  4.813960e-08
  14  5nug    8760   56979  0.039969  1.778400e-10  1.797600e-06
  15  4rh7    9015   59346  0.041572  8.694090e-11  6.179150e-07
  16  5np0    7584   59478  0.048659  4.370420e-11  2.258690e-07
  17  3vkh    9126   59592  0.069080  1.717250e-09  1.228240e-05

TABLE DATA_EPSD_00_DMAX_60.csv ==============================
     pid  nnodes  nedges      tsec           mde           lde
0   1n6t      30     236  0.000214  8.090110e-12  3.638360e-10
1   1fw5      60     558  0.000508  3.468890e-12  1.102170e-10
2   1adx     120    1008  0.000871  6.108290e-12  8.793430e-10
3   1bdo     241    2167  0.001895  1.316690e-11  7.048610e-10
4   1all     480    4932  0.004593  3.439390e-12  3.763010e-09
5   6s61     522    5298  0.004874  7.102120e-12  5.008250e-09
6   4wua    1033    9727  0.008663  6.098920e-12  2.822310e-09
7   1fhl    1002    9811  0.009024  1.713600e-11  4.041950e-09
8   6czf    1494   14163  0.012722  4.141510e-12  1.615980e-09
9   5ijn    1950   18266  0.016346  1.794020e-11  7.339180e-09
10  6rn2    2052   19919  0.017698  1.157100e-11  5.967810e-09
11  1cza    2694   26452  0.023335  6.112460e-11  2.188770e-08
12  6bco    2856   27090  0.024079  1.448640e-11  2.383370e-08
13  1epw    3861   35028  0.030875  1.938080e-10  6.064320e-08
14  5np0    7584   80337  0.073235  1.467060e-10  3.822400e-07
15  5nug    8760   82717  0.070263  6.074620e-10  2.490100e-06
16  4rh7    9015   85831  0.075049  2.151470e-10  7.745170e-07
17  3vkh    9126   87621  0.076556  8.921410e-10  7.545720e-06
