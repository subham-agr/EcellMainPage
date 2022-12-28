import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-gallery',
  templateUrl: './gallery.component.html',
  styleUrls: ['./gallery.component.scss']
})
export class GalleryComponent implements OnInit {

  images:any; 
  responsiveOptions:any;

  li:any;
  lis:[];

  constructor(private http: HttpClient) { 
    
  }

  ngOnInit(): void {
    this.http.get('http://localhost:8000/gallery').subscribe(Response => {
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
