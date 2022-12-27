import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-gallery',
  templateUrl: './gallery.component.html',
  styleUrls: ['./gallery.component.scss']
})
export class GalleryComponent implements OnInit {

  constructor(private http: HttpClient) { }
  li:any;
  lis=[];

  ngOnInit(): void {
    const headers = { Authorization: "Token " + localStorage.getItem("authToken") }
    this.http.get('https://api3.ecell.in/eureka22/getFaq/')
    .subscribe(Response => {
      console.log(Response)
      this.li=Response;
      this.lis=this.li.faq;
      console.log(this.lis)
    });

  }

}
