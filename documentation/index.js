
/**
 * @api {post} http://127.0.0.1:8000/answer login.
 * @apiVersion 1.0.0
 * @apiName login
 * @apiGroup Login
 * 
 * @apiDescription 
 * Nos va a permitir loguearnos.
 * @apiParam {String} user Nombre del usuario
 * @apiParam {String} paswword Contraseña
 * @apiSuccessExample Success-Response:
 *     HTTP/1.1 200 OK
 *  {
    "status": "200",
    "msg": "Acceso correcto",
    "data": [
        {
            "token": "\"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoicGpndCIsInBhc3N3b3JkIjoiMTIzNDU2In0.3GoXdwjFeah3vNKt0mqGzLzMNPwEretf7VQUGLZzfws\"",
            "status": 201
        }
    ]
}
 */



/**
 * @api {post} http://127.0.0.1:8000/course course.
 * @apiVersion 1.0.0
 * @apiName course
 * @apiGroup Course
 * 
 * @apiDescription 
 * Nos va a permitir crear cursos.
 * @apiParam {String} name Nombre del curso
 * @apiParam {int} depend Indica si el curso es dependiente de otro: 1 que si es dependiente 0 que no es dependiente
 * @apiParam {String} uuidCourse Nos va a indicar si es dependiente el curso de que curso se hace referencia
 * @apiSuccessExample Success-Response:
 *     HTTP/1.1 200 OK
 *  {
    "status": "200",
    "msg": "New register",
    "data": []
}
 */


/**
 * @api {post} http://127.0.0.1:8000/lesson lesson.
 * @apiVersion 1.0.0
 * @apiName lesson
 * @apiGroup Lesson
 * 
 * @apiDescription 
 * Nos va a permitir crear una leccion
 * @apiParam {String} uuidCourse El curso con que queremos vicular esta leccion
 * @apiParam {String} name El nombre de la leccion
 * @apiParam {int} depend Indica si la leccion es dependiente de otro: 1 que si es dependiente 0 que no es dependiente
 * @apiParam {String} uuidLesson Nos va a ayudar a vincular con que otra leccion esta vinculada.
 * @apiSuccessExample Success-Response:
 *     HTTP/1.1 200 OK
 *  {
    "status": "200",
    "msg": "New register",
    "data": []
}
 */


/**
 * @api {post} http://127.0.0.1:8000/questions question.
 * @apiVersion 1.0.0
 * @apiName question
 * @apiGroup Question
 * 
 * @apiDescription 
 * Nos va a permitir crear preguntas acerca de la leccion
 * @apiParam {String} question El nombre de la pregunta
 * @apiParam {int} score Indica el puntuaje de la pregunta
 * @apiParam {String} uuidLesson Indica a que leccion le pertenece la pregunta
 * @apiSuccessExample Success-Response:
 *     HTTP/1.1 200 OK
 *  {
    "status": "200",
    "msg": "New register",
    "data": []
}
 */


/**
 * @api {post} http://127.0.0.1:8000/type TypeAnswer.
 * @apiVersion 1.0.0
 * @apiName Type_answer
 * @apiGroup Type_answer
 * @apiDescription 
 * Nos va a permitir crear los tipos de respuestas que existen en el cuestionario
 * @apiParam {String} name El nombre de la respuesta Unico, Multiple
 * @apiSuccessExample Success-Response:
 *     HTTP/1.1 200 OK
 *  {
    "status": "200",
    "msg": "New register",
    "data": []
}
 */



/**
 * @api {post} http://127.0.0.1:8000/answer Answer
 * @apiVersion 1.0.0
 * @apiName Answer
 * @apiGroup Answer
 * @apiDescription 
 * Nos va a permitir registrar las respuestas de las preguntas e indicar cual es la correcta
 * @apiParam {String} uuidQuestion Indica a que pregunta se le va a vincular la respuesta
 * @apiParam {String} answer La descripcion de la respuesta
 * @apiParam {Int} isCorrect Indica si la respuesta es la correcta o no. 0 no es correcta 1 si es correcta
 * @apiSuccessExample Success-Response:
 *     HTTP/1.1 200 OK
 *  {
    "status": "200",
    "msg": "New register",
    "data": []
}
 */