require 'thor'
require 'io/console'

module Nexy
  require 'nexy/version'

  class ThorShell < Thor::Shell::Color

    def ask_securely(*args)
      # TODO: Ask args and securely get response
      STDIN.noecho(&:gets).chomp
    end

    def ask_yes_or_no(statement, color = :white)
      response = ask(statement, color)
      while validate_yes_no(response)
        say("Your response to that question: #{response} should be a \"y\", \"yes\", \"n\" or \"no\", please enter again.", :yellow)
        response = ask(statement, color)
      end
      response =~ /^y$|^yes$/
    end

    def ask_yes_or_no_with_default(statement, default='y')
      responses = ['y', 'n'].map{ |s| s == default ? s.upcase : s }
      response = ask("#{statement} [#{responses.join}]").downcase
      response = default if response.empty?
      response == 'y'
    end

    private

    def validate_yes_no(string)
      !(string =~ /^y$|^yes$|^no$|^n$/)
    end

    # TODO: These should be moved to the create subcommand
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
