import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-drive-element',
  templateUrl: './drive-element.component.html',
  styleUrls: ['./drive-element.component.css']
})
export class DriveElementComponent implements OnInit {


  fileList = [{name: 'file1.txt', size: '10 kb', creationDate: '12/12/12'},
              {name: 'file2.txt', size: '100 kb', creationDate: '12/12/12'},
              {name: 'file3.txt', size: '1000 kb', creationDate: '12/12/12'}];
  constructor() { }

  ngOnInit() {
  }

}
