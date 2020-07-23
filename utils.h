#pragma once

#include <vector>
#include <string>
#include <stdexcept>
#include <execinfo.h>
#include <omp.h>

#define FMT_RESET   "\033[0m"
#define FMT_BLACK   "\033[30m"      /* Black */
#define FMT_RED     "\033[31m"      /* Red */
#define FMT_GREEN   "\033[32m"      /* Green */
#define FMT_YELLOW  "\033[33m"      /* Yellow */
#define FMT_BLUE    "\033[34m"      /* Blue */
#define FMT_MAGENTA "\033[35m"      /* Magenta */
#define FMT_CYAN    "\033[36m"      /* Cyan */
#define FMT_WHITE   "\033[37m"      /* White */
#define FMT_BOLD_BLACK   "\033[1m\033[30m"      /* Bold Black */
#define FMT_BOLD_RED     "\033[1m\033[31m"      /* Bold Red */
#define FMT_BOLD_GREEN   "\033[1m\033[32m"      /* Bold Green */
#define FMT_BOLD_YELLOW  "\033[1m\033[33m"      /* Bold Yellow */
#define FMT_BOLD_BLUE    "\033[1m\033[34m"      /* Bold Blue */
#define FMT_BOLD_MAGENTA "\033[1m\033[35m"      /* Bold Magenta */
#define FMT_BOLD_CYAN    "\033[1m\033[36m"      /* Bold Cyan */
#define FMT_BOLD_WHITE   "\033[1m\033[37m"      /* Bold White */

#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define SQR(a) ((a) * (a))
#define THROW_EXCEPTION(msg) throw_exception_backtrace((msg), __FILE__, __LINE__)

void throw_exception_backtrace(std::string msg, std::string const file, int line)
{
#pragma omp critical(throw_exception)
   {
      char MSG[256];
      sprintf(MSG, FMT_BOLD_RED "[%s:%d, thread = %d] %s" FMT_RESET, file.c_str(), line, omp_get_thread_num(), msg.c_str());

      const int buffer_size = 1024;
      int nptrs;
      void *buffer[buffer_size];
      char **strings;

      nptrs = backtrace(buffer, buffer_size);
      printf("backtrace() returned %d addresses\n", nptrs);

      /* The call backtrace_symbols_fd(buffer, nptrs, STDOUT_FILENO)
              would produce similar output to the following: */

      strings = backtrace_symbols(buffer, nptrs);
      if (strings == NULL)
      {
         perror("backtrace_symbols");
         exit(EXIT_FAILURE);
      }

      for (int j = 0; j < nptrs; j++)
         printf("[bt] (%d) %s\n", j, strings[j]);

      free(strings);

      throw std::runtime_error(MSG);
   }
}

class options_t
{
 public:
   options_t(int argc, char *argv[]) : m_args(argc)
   {
      for (int i = 0; i < argc; ++i)
         m_args[i] = std::string(argv[i]);
   }

   int read_param(std::string name, int value)
   {
      for (size_t i = 0; i < m_args.size(); ++i)
      {
         if (name.compare(m_args[i]) == 0)
            value = stod(m_args[i + 1]);
      }
      return value;
   }

   double read_param(std::string name, double value)
   {
      for (size_t i = 0; i < m_args.size(); ++i)
         {
            if (name.compare(m_args[i]) == 0)
               value = stod(m_args[i + 1]);
         }
      return value;
   }

   std::string read_param(std::string name, std::string value)
   {
      for (size_t i = 0; i < m_args.size(); ++i)
      {
         if (name.compare(m_args[i]) == 0)
            value = m_args[i + 1];
      }
      return value;
   }

   std::vector<std::string> m_args;
};
