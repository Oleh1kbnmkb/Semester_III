import { Component } from '@angular/core';
import { Housinglocation } from '../housinglocation';
import { HousingLocationComponent } from "../housing-location/housing-location.component";

@Component({
    selector: 'app-home',
    standalone: true,
    template: `
   
  <section class="results">
    <app-housing-location [housingLocation]="housingLocation"></app-housing-location>    
  </section>
    
  `,
    styleUrl: './home.component.css',
    imports: [HousingLocationComponent]
})
export class HomeComponent {
  readonly baseUrl = "http://localhost:4200/assets";
  housingLocation: Housinglocation = {
    id: 9999,
    name: "Test Home",
    city: "Test City",
    state: "ST",
    photo: "${this.baseUrl}/example-house.jpg",
    wifi: true,
    laundry: false,
    aviableUnits: 99
  }
}
