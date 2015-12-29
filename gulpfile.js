var gulp = require('gulp'),
    less = require('gulp-less');


gulp.task('update-styles', function () {
    return gulp.src('bower_components/bootstrap/less/bootstrap.less')
        .pipe(less())
        .pipe(gulp.dest('bower_components/bootstrap/dist/css/'));
});

gulp.task('stage-css', function () {
    var sources = [
        'bower_components/bootstrap/dist/css/bootstrap.css',
        'bower_components/font-awesome/css/font-awesome.css'
    ];
    return gulp.src(sources).pipe(gulp.dest('web/static/web/css'));
});

gulp.task('stage-js', function () {
    var sources = [
        'bower_components/jquery/dist/jquery.js',
        'bower_components/bootstrap/dist/js/bootstrap.js'
    ];
    return gulp.src(sources).pipe(gulp.dest('web/static/web/js'));
});

gulp.task('stage-fonts', function () {
    var sources = [
        'bower_components/bootstrap/dist/fonts/*.*',
        'bower_components/font-awesome/fonts/*.*'
    ];
    return gulp.src(sources).pipe(gulp.dest('web/static/web/fonts'));
});

gulp.task('stage', ['stage-fonts', 'stage-css', 'stage-js']);