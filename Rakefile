task default: "assets:precompile"

namespace :assets do
  desc "Precompile assets"
  task :precompile do
    sh "bundle exec jekyll build --config src/common/_config.yml,src/site/_config.yml"
    sh "bundle exec jekyll build --config src/common/_config.yml,src/blog/_config.yml"

    # Unfortunately jekyll doesnt support multiple sources yet, and overwrites
    # things if destinations collide, so the only way to get the css into _site
    # is to just blindly copy it.
    # TODO: If https://github.com/mojombo/jekyll/issues/1420 is resolved, fix
    FileUtils.mkdir_p("_site/css")
    FileList["src/common/css/*"].each do |source|
      target = "_site/css/" + source.split("/").last
      cp source, target
    end

    # TODO: Serve images better
    FileUtils.cp_r("media", "_site/media");
  end
end
