require 'thor'
require 'io/console'
require 'nexy/version'

module Nexy
  class ThorShell < Thor::Shell::Color

    def ask_securely(*args)
      # TODO: Ask args and securely get response
      STDIN.noecho(&:gets).chomp
    end

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
