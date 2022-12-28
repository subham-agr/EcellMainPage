import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  constructor() { }
  scrollToBottom() {
    window.scrollTo(0, document.body.scrollHeight);
  }

  ngOnInit(): void {
  }

}
