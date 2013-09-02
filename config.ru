require 'rack/contrib/try_static'
require 'rack/contrib/not_found'
require 'rack/rewrite'

require 'newrelic_rpm'

use Rack::Rewrite do
  # Redirect all non-www traffic to www.
  r301 %r{.*}, 'http://www.stephenmcgruer.com$&', :if => Proc.new { |rack_env|
    ENV['RACK_ENV'] == "production" and
    rack_env['SERVER'] != 'www.stephenmcgruer.com'
  }
end

use Rack::TryStatic,
  :root => "_site",
  :urls => %w[/],
  :try => ['index.html', '/index.html']

run Rack::NotFound.new('_site/404.html')
