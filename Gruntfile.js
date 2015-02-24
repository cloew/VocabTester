module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        project: {
            src: 'src',
            serverStatic: '<%= project.src %>/Server/static',
            stylesheets: '<%= project.serverStatic %>/stylesheets',
            js: '<%= project.serverStatic %>/js/*.js'
        },
        sass: {
            dist: {
                files: [{
                    expand: true,
                    cwd: '<%= project.stylesheets %>',
                    src: ['*.scss'],
                    dest: '<%= project.stylesheets %>',
                    ext: '.css'
                }]
            }
        }
  });
  grunt.loadNpmTasks('grunt-contrib-sass');

  // Default task(s).
  grunt.registerTask('default', ['sass']);

};