import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-drive-element',
  templateUrl: './drive-element.component.html',
  styleUrls: ['./drive-element.component.css']
})
export class DriveElementComponent implements OnInit {
  fileList = ['fileone.txt', 'file2.py', 'file3.exe']
  constructor() { }

  ngOnInit() {
  }

}
