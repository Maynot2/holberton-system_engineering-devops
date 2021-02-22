#!/usr/bin/env ruby

if ARGV
	puts "#{ARGV[0]}".scan(/\[from:(\S+)\] \[to:(\S+)\] \[flags:(\S+)\] /).join(",")
end
