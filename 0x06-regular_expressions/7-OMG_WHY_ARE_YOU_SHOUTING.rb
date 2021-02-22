#!/usr/bin/env ruby

if ARGV
	puts "#{ARGV[0]}".scan(/[A-Z]/).join
end
