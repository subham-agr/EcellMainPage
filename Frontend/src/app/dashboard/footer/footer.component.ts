import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.scss']
})
export class FooterComponent implements OnInit {

  li:any;
  email = "email";
  constructor(private http:HttpClient) { }

  ngOnInit(): void {
    this.http.get("http://localhost:8000/query").subscribe(Response => {
      this.li = Response;
      console.log(Response)
    })
  }

}
