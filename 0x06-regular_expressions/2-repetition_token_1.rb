#!/usr/bin/env ruby

if ARGV
	puts "#{ARGV[0]}".scan(/hb?tn/).join
end
