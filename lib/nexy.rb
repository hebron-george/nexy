require 'thor'
require 'nexy/version'

module Nexy
  class ThorShell < Thor

    def ask_securely(*args)
      # TODO: Ask args and securely get response
      STDIN.noecho(&:gets).chomp
    end
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

    private

    def create_project!(project_configuration)

    end

    def create_project_config(project_details = {})
      errors = []
      errors << :missing_project_name unless project_name = project_details[:name]
      errors << :missing_project_type unless project_type = project_details[:type]

      raise StandardError.new("Could not create project config: #{errors.map(&:to_s)}") if errors.any?

      puts "Creating config for a #{project_type} project called #{project_name}"

      {
          :name => project_name,
          :type => project_type,
      }
    end

    def create_project_from_config!(config)

    end
  end

  def self.ui
    @ui ||= ThorShell.new
  end

  def self.cli_root
    File.dirname __dir__
  end
end
