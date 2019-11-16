extern crate actix_web;
use actix_web::{HttpServer, App, web, HttpRequest, HttpResponse};

crate drive 


fn index(_req: HttpRequest) -> HttpResponse  {
    HttpResponse::Ok().json("Hello world!")
}

fn t1(_req: HttpRequest) -> HttpResponse  {
    HttpResponse::Ok().json("Hello world! T111111111")
}

fn t2(_req: HttpRequest) -> HttpResponse  {
    HttpResponse::Ok().json("Hello world! T222222222222")
}

fn main(){
    f = drive::files::File::new()
    f.create("FOOOOOOOOOOOOOOOOOOOO")
    HttpServer::new(|| App::new()
        .service(web::resource("/").route(web::get().to_async(index)))
        .service(web::resource("/t1").route(web::get().to_async(t1)))
        .service(web::resource("/t2").route(web::get().to_async(t2)))
        )
    .bind("127.0.0.1:8088")
    .unwrap()
    .run();
}   