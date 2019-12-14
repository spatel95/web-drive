import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DriveElementComponent } from './drive-element/drive-element.component';
import {MatExpansionModule} from '@angular/material/expansion';
import { MatSliderModule } from '@angular/material/slider';



@NgModule({
  declarations: [DriveElementComponent],
  imports: [
    CommonModule,
    MatExpansionModule,
  ],
  exports: [DriveElementComponent]
})
export class FilesModule { }
export {DriveElementComponent};
