#!/usr/bin/env ruby

if ARGV
	puts "#{ARGV[0]}".scan(/\A\d{10}\z/).join
end
