require 'thor'
require 'nexy'

module Nexy
  class CLI < Thor
    include Thor::Actions

    desc 'version', 'Prints current nexy version'
    def version
      say("nexy v#{Nexy::VERSION} running Ruby v#{RUBY_VERSION} on #{RUBY_PLATFORM}")
    end

    desc 'setup', 'Walk through nexy configuration setup'
    long_desc <<-LONGDESC
  nexy will walk you step-by-step through configuration in a very simple
  question-answer format.
    LONGDESC
    def setup(*args)
      require 'nexy/cli/setup'
      Nexy::CLI::Setup.run(args)
    end

    desc 'create', 'Start a new project'
    long_desc <<-LONGDESC
      Starting a new project from scratch can be a painful task.\n
      nexy will help you get started as quickly as possible.\n
      Currently supports:\n
        - Plain old Ruby\n
        - Ruby on Rails\n
        - Plain old Python\n
    LONGDESC
    def create(*args)

    end

    # TODO: Make these subcommands -- http://whatisthor.com/
    desc 'create-ruby-app <name>', 'create a new plain old Ruby project'
    def create_ruby_app(name)
      type = :ruby.freeze
      config = create_project_config(name: name, type: type)
    end

    desc 'create-rails-app <name>', 'create a new Ruby on Rails application'
    def create_rails_app(name)
      type = :rails.freeze
      config = create_project_config(name: name, type: type)
    end

    desc 'create-python-app <name>', 'create a new plain old Python project'
    def create_python_app(name)
      type = :python.freeze
      config = create_project_config(name: name, type: type)
    end
  end
end
