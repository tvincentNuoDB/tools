#include <stdio.h>
#include <sys/time.h>

typedef long long int64;
typedef unsigned long long uint64;
uint64 master;

uint64 getTimeMs64(){
 struct timeval tv; 

 gettimeofday(&tv, NULL);

 uint64 ret = tv.tv_usec;
 /* Convert from micro seconds (10^-6) to milliseconds (10^-3) */
 ret /= 1000;

 /* Adds the seconds (10^0) after converting them to milliseconds (10^-3) */
 ret += (tv.tv_sec * 1000);

 return ret;
}

double runRuby();
double runPython();
double runJava();

int main() {
	double rubyTime = runRuby();
	printf("Finished ruby!\n");
	double pythonTime = runPython();
	printf("Finished python!\n");
	double javaTime = runJava();
	printf("Finished Java!\n");

	printf("RUBY:%.2fs\nPYTHON:%.2fs\nJAVA:%.2fs\n", rubyTime, pythonTime, javaTime);
	return 0;
}

double runRuby() {
	master = getTimeMs64();
	system("ruby rbyBenchmark.rb");
	return ((getTimeMs64() - master) * 0.001);
}

double runPython() {
	master = getTimeMs64();
	system("python pyBenchmark.py");
	return ((getTimeMs64() - master) * 0.001);
}

double runJava() {
	master = getTimeMs64();
	system("java jvBenchmark");
	return ((getTimeMs64() - master) * 0.001);
}
