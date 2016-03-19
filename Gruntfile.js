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
            serverDir: '<%= project.src %>/Server',
            serverStatic: '<%= project.serverDir %>/static',
            stylesheets: '<%= project.serverStatic %>/stylesheets',
            js: '<%= project.serverStatic %>/js'
        },
        bowercopy: {
            options: {
                srcPrefix: 'bower_components'
            },
            js: {
                files: {
                  'src/Server/static/lib': '*/dist/*.js'
                }
            },
            "ng-autofocus": {
                files: {
                  'src/Server/static/lib/': 'ng-autofocus/dist/ng-autofocus.min.js'
                }
            },
            "kao-ng-crud": {
                files: {
                  'src/Server/static/lib/kao-crud': 'kao-ng-crud/dist/*.js'
                }
            },
            "traceur-runtime": {
                files: {
                  'src/Server/static/lib': 'traceur-runtime/traceur-runtime.js'
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
        },
        ngtemplates:  {
            VocabTester: {
                cwd: '<%= project.serverDir %>',
                src: 'static/partials/**/*.html',
                dest: '<%= project.js %>/templates.js',
            }
        }
    });
    grunt.loadNpmTasks('grunt-bowercopy');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-spider-script');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-angular-templates');

    // Default task(s).
    grunt.registerTask('html', ['ngtemplates']);
    grunt.registerTask('spider', ['spider_script']);
    grunt.registerTask('js', ['bowercopy', 'spider']);
    grunt.registerTask('local', ['sass', 'spider', 'html']);
    grunt.registerTask('default', ['bowercopy', 'local']);
};