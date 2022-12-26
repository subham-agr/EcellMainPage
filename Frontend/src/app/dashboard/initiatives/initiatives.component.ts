import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-initiatives',
  templateUrl: './initiatives.component.html',
  styleUrls: ['./initiatives.component.scss']
})
export class InitiativesComponent implements OnInit {


  li:any;
  lis:[];
  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.http.get('http://localhost:8000/home').subscribe(Response => {
      this.li = Response;
      this.lis = this.li[0];
      console.log(Response)
      console.log(this.lis)
    })
  }

}
