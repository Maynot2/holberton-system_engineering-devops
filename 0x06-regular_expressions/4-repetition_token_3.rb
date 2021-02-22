#!/usr/bin/env ruby

if ARGV
	puts "#{ARGV[0]}".scan(/hbt*n/).join
end
