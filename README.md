# genomic_coverage

Genomic coverage in NGS data 

### Prompt

This was a prompt to calculate the 'coverage,' or 'read depth'  of genome data. I was provided with a csv document including the starting position of a genome sequence and its length, and was asked to create a function that would specify how many reads any given location has.

### problem solving

I approached this task by using python's dictionary function because it uses hashing to compare values. I have two main functions. The first reads through the csv and adds a count of each genome location. The second is the search method, which was a simple dictionary search. For comparison I also wrote a binary search function to compare speeds. 

### testing

I was also given some correct values to perform tests with. I use the timeit library for speed testing.
