#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regular expression,
# matching method
# The regular expression  matches the given cases

puts ARGV[0].scan(/hbt+n/).join
