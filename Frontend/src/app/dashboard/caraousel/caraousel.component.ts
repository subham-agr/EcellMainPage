import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-caraousel',
  templateUrl: './caraousel.component.html',
  styleUrls: ['./caraousel.component.scss']
})
export class CaraouselComponent implements OnInit {
  images:any; 
  responsiveOptions:any;

  li:any;
  lis:[];

  constructor(private http: HttpClient) { 
    this.responsiveOptions = [
      {
          breakpoint: '1024px',
          numVisible: 3,
          numScroll: 3
      },
      {
          breakpoint: '768px',
          numVisible: 2,
          numScroll: 2
      },
      {
          breakpoint: '560px',
          numVisible: 1,
          numScroll: 1
      }
  ];
  }

  ngOnInit(): void {
    this.http.get('http://localhost:8000/initiatives').subscribe(Response => {
      this.li = Response;
      console.log(Response)
    })
    this.images = [
      {random: 'Random', picture: 'https://picsum.photos/id/944/900/500'},
      {random: 'Samoa', picture: 'https://picsum.photos/id/1011/900/500'},
      {random: 'Tonga', picture: 'https://picsum.photos/id/984/900/500'},
      {random: 'Cook Island', picture: 'https://picsum.photos/id/944/900/500'},
      {random: 'Niue', picture: 'https://picsum.photos/id/1011/900/500'},
      {random: 'American Samoa', picture: 'https://picsum.photos/id/984/900/500'}
  ];
  }

}
