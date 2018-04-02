require 'nexy/cli'

module Nexy
  class CLI::Base
    def self.run(options)
      new(options).run
    end

    attr_reader :options
    def initialize(options)
      @options = options.dup
    end

    def ui
      ::Nexy.ui
    end

    def run
      raise NotImplementedError, 'Must be implemented by a subclass'
    end
  end
end
