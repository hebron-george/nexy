require 'nexy/cli/base'

module Nexy
  class CLI::Setup < CLI::Base
    CONFIG_FILE = '~/.nexy'.freeze

    def run
      ui.say('Beginning setup...')
    end
  end
end
