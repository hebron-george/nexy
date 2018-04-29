require 'yaml'
require 'awesome_print'

module Nexy
  module Config
    extend self

    CONFIG_PATH      = '~/.nexy'
    FULL_CONFIG_PATH = File.expand_path(CONFIG_PATH)

    FIELDS = %w{ projects_path }

    def config_object
      if config_file_exists?
        @config_object ||= read_config_file
      else
        @config_object ||= default_config
      end
    end

    def config_file_exists?
      File.file?(FULL_CONFIG_PATH)
    end

    def write_config_file
      File.open(FULL_CONFIG_PATH, 'w') { |f| f.write config_object.to_yaml }
    end

    def pretty_print
      config_object.ai
    end

    def for_each_field(&block)
      FIELDS.each { |f| block.call(f) if block_given? }
    end

    # This will build all of the accessors for generic fields. If you need custom
    # functionality, just define the accessor method above this code and name it
    # appropriately.
    # my_field_exists?
    # my_field    -reader
    # my_field=   -writer
    (FIELDS).each do |field|
      unless self.method_defined?("#{field}_exists?")
        define_method("#{field}_exists?") do
          config_file_exists? && config_object.has_key?(field)
        end
      end

      unless self.method_defined?(field)
        define_method(field) do
          config_object.fetch(field, nil)
        end
      end

      unless self.method_defined?("#{field}=")
        define_method("#{field}=") do |value|
          config_object[field] = value
        end
      end
    end

    private

    def read_config_file
      YAML.load_file(FULL_CONFIG_PATH) || default_config
    end

    def default_config
      Hash.new
    end
  end
end
