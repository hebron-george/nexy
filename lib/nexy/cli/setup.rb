require 'nexy/cli/base'

module Nexy
  class CLI::Setup < CLI::Base
    def run
      Nexy::Config.config_file_exists? ? update_existing_config! : create_new_config!
      ui.say("You're ready to start!", :green)
      ui.say(Nexy::Config.pretty_print)
    end

    private

    def update_existing_config!
      ui.say("An existing config file was found at: #{Nexy::Config::CONFIG_PATH}")
      ui.say(Nexy::Config.pretty_print)
      configure_fields
      Nexy::Config.write_config_file
    end

    def create_new_config!
      ui.say("Let's set up nexy to work for you!")
      configure_fields
      Nexy::Config.write_config_file
    end

    def configure_fields
      Nexy::Config.for_each_field do |field|
        next if !ui.ask_yes_or_no("Configure #{field} (y or n)?")
        response = false
        response = enter_new_value(field) while !response
      end
    end

    def enter_new_value(field)
      new_value = ui.ask("Enter your #{field}: ")
      Nexy::Config.send("#{field}=", new_value)
      ui.say("The #{field} you entered is: #{new_value}.", :blue)
      ui.ask_yes_or_no("Is this correct? (y or n)", :blue)
    end
  end
end
