task default: "assets:precompile"

namespace :assets do
  desc "Precompile assets"
  task :precompile do
    sh "bundle exec jekyll build --config src/common/_config.yml,src/site/_config.yml"
    sh "bundle exec jekyll build --config src/common/_config.yml,src/blog/_config.yml"
  end
end
