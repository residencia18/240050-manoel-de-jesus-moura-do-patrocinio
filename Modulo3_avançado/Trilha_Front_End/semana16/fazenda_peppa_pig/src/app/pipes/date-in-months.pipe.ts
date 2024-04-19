import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'dateInMonths',
  standalone: true
})
export class DateInMonthsPipe implements PipeTransform {

  transform(value: Date): number | null {
    if (!value) return null;
    const date:Date = new Date(value);
    const today = new Date();
    const years = today.getFullYear() - date.getFullYear();
    const months = today.getMonth() - date.getMonth();

    
    const AgeInmonths = years * 12 + months;

    return AgeInmonths;
  }

}
