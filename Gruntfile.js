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
    },
    watch: {
        sass: {
            files: '<%= project.stylesheets %>/*.{scss,sass}',
            tasks: ['sass']
        }
    }
  });
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Default task(s).
  grunt.registerTask('default', ['sass']);

};