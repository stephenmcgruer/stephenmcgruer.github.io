task default: "assets:precompile"

namespace :assets do
  desc "Precompile assets"
  task :precompile do
    sh "bundle exec jekyll build --config src/site/_config.yml"
  end
end
