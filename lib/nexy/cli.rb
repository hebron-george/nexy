require 'thor'
require 'nexy'

module Nexy
  class CLI < Thor
    include Thor::Actions

    desc 'setup', 'Walk through nexy configuration setup'
    def setup
      # config = get_current_config
      # update_config! config
    end

    desc "create-ruby-app <name>", "create a new plain old Ruby project"
    def create_ruby_app(name)
      type = :ruby.freeze
      config = create_project_config(name: name, type: type)
    end

    desc "create-rails-app <name>", "create a new Ruby on Rails application"
    def create_rails_app(name)
      type = :rails.freeze
      config = create_project_config(name: name, type: type)
    end

    desc "create-python-app <name>", "create a new plain old Python project"
    def create_python_app(name)
      type = :python.freeze
      config = create_project_config(name: name, type: type)
    end
  end
end
