require 'nexy/cli/base'

module Nexy
  class CLI::Create < CLI::Base
    def self.required_keys
      ['projects_path']
    end

    def run
      ui.say("Let's create a new project!")
    end

    private

    def does_project_already_exist?

    end
  end
end
