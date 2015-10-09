module.exports = function(grunt) {

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        project: {
            src: 'src',
            webapp: '<%= project.src %>/WebApp',
            spider: '<%= project.webapp %>/spider',
            sass: '<%= project.webapp %>/stylesheets',
            sassLib: '<%= project.webapp %>/stylesheets/lib',
            serverStatic: '<%= project.src %>/Server/static',
            stylesheets: '<%= project.serverStatic %>/stylesheets',
            js: '<%= project.serverStatic %>/js'
        },
        bowercopy: {
            options: {
                srcPrefix: 'bower_components'
            },
            js: {
                options: {
                    destPrefix: 'src/Server/static/lib'
                },
                files: {
                  'src/Server/static/lib': '*/dist/*.js'
                }
            },
            css: {
                files: [{
                    expand: true,
                    src: ['**/*.css'],
                    dest: '<%= project.stylesheets %>',
                    ext: '.css'
                }]
            },
            scss: {
                files: [{
                    expand: true,
                    src: ['**/*.scss'],
                    dest: '<%= project.sassLib %>',
                    ext: '.scss'
                }]
            }
        },
        sass: {
            compile: {
                files: [{
                    expand: true,
                    cwd: '<%= project.sass %>',
                    src: ['**/*.scss'],
                    dest: '<%= project.stylesheets %>',
                    ext: '.css'
                }]
            }
        },
        spider_script: {
            options: {
                sourcemap: false
            },
            compile: {
                files: [{
                    expand: true,
                    cwd: '<%= project.spider %>',
                    src: ['**/*.spider'],
                    dest: '<%= project.js %>',
                    ext: '.js'
                }]
            }
        }
    });
    grunt.loadNpmTasks('grunt-bowercopy');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-spider-script');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Default task(s).
    grunt.registerTask('default', ['bowercopy', 'sass', 'spider_script']);
    grunt.registerTask('spider', ['spider_script']);
};