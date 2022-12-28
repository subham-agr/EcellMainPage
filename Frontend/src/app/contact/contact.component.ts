import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.scss']
})
export class ContactComponent implements OnInit {

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
