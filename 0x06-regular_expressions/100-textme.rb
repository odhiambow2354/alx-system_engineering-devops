#!/usr/bin/env ruby
# The script accepts one argument and passes it to a regular expression,
# matching method
# Your script should output: [SENDER],[RECEIVER],[FLAGS]
# The sender phone number or name 
# The receiver phone number or name
# The flags used

sender = ARGV[0].scan(/(?<=\[from:)[^ ]+(?=\])/).join
reciever = ARGV[0].scan(/(?<=\[to:)[^ ]+(?=\])/).join
flags = ARGV[0].scan(/(?<=\[flags:)[^ ]+(?=\])/).join
puts "#{sender},#{reciever},#{flags}"
