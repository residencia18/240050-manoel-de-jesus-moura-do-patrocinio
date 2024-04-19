import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ManegerManejoComponent } from './maneger-manejo.component';

describe('ManegerManejoComponent', () => {
  let component: ManegerManejoComponent;
  let fixture: ComponentFixture<ManegerManejoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ManegerManejoComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ManegerManejoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
