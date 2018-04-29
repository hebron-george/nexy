require 'nexy/cli'
require 'nexy/config'

module Nexy
  class CLI::Base
    def self.run(options)
      abort "Your setup is incomplete, try: `nexy setup`" unless required_keys.all? { |key| Nexy::Config.config_object.keys.include? key }
      new(options).run
    end

    # The required keys needed in our
    # config file (Nexy::Config.config_object)
    # in order for this class (or it's descendants)
    # to properly function.
    #
    # E.g. the `create` function creates new projects,
    # therefore it requires that the `projects_path`
    # be configured, otherwise it doesn't know where to
    # create the project.
    def self.required_keys
      []
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
