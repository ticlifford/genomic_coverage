# Genomic_coverage

(95% of the code is in coverage_counter.py if you just want to take a peak)

Genomic coverage in NGS data 

### Prompt

This was a prompt to calculate the 'coverage,' or 'read depth'  of genome data. I was provided with a csv document including the starting position of a genome sequence and its length, and was asked to create a function that would specify how many reads any given location has. The reads.csv file is like 20GB so I didn't include it.

### Problem solving

I approached this task by using python's dictionary function because it uses hashing to compare values. I have two main functions. The first reads through the csv and adds a count of each genome location. The second is the search method, which was a simple dictionary search. For comparison I also wrote a binary search function to compare speeds. 

### Testing

I was also given some correct values to perform tests with. I use the timeit library for speed testing.

### Thoughts

This was an interesting little prompt. The provided reads.csv was too big to be included here so this won't actually run. This is designed to run with just the basic python install, there are probably faster ways of performing this csv read. One idea that I didn't persue because of time was compressing the data by finding duplicate reads. In the document there are tons of duplicate reads, both in location and length. I could have had it first counted the duplicate pairs and then performed a quicker dictionary operation, but what stopped me was knowing how valuable this would be. The original reads.csv was gigantic, and I would have needed to spend some time in pandas to get a gist for how much time that would have saved.
