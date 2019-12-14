import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DriveElementComponent } from './drive-element.component';

describe('DriveElementComponent', () => {
  let component: DriveElementComponent;
  let fixture: ComponentFixture<DriveElementComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DriveElementComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DriveElementComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
