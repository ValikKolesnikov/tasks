let gulp = require('gulp'), // Подключаем Gulp
    sass = require('gulp-sass');


gulp.task('sass', function () {
    return gulp.src('./**/**.sass') // Берем все styles файлы из папки styles и дочерних, если таковые будут
        .pipe(sass())
        .pipe(gulp.dest('.'))
});


gulp.task('watch', function () {
    gulp.watch('./**/*.sass', gulp.parallel('sass'));

});


