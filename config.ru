require 'rack/contrib/try_static'
require 'rack/contrib/not_found'

require 'newrelic_rpm'

STDOUT.puts "RPM detected environment: #{NewRelic::LocalEnvironment.new}"

use Rack::TryStatic,
  :root => "_site",
  :urls => %w[/],
  :try => ['index.html', '/index.html']

run Rack::NotFound.new('_site/404.html')
