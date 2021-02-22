#!/usr/bin/env ruby

if ARGV
	puts "#{ARGV[0]}".scan(/hbt{2,5}n/).join
end
