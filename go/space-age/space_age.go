package space

type Planet string

func Age(seconds float64, planet Planet) float64 {
	var age_on_planet float64
	if planet == "Earth" {
		age_on_planet = seconds / 31557600
		return age_on_planet
	}

	if planet == "Mercury" {
		age_on_planet = seconds / 31557600 / 0.2408467
		return age_on_planet
	}

	if planet == "Venus" {
		age_on_planet = seconds / 31557600 / 0.61519726
		return age_on_planet
	}

	if planet == "Mars" {
		age_on_planet = seconds / 31557600 / 1.8808158
		return age_on_planet
	}

	if planet == "Jupiter" {
		age_on_planet = seconds / 31557600 / 11.862615
		return age_on_planet
	}

	if planet == "Saturn" {
		age_on_planet = seconds / 31557600 / 29.447498
		return age_on_planet
	}

	if planet == "Uranus" {
		age_on_planet = seconds / 31557600 / 84.016846
		return age_on_planet
	}

	if planet == "Neptune" {
		age_on_planet = seconds / 31557600 / 164.79132
		return age_on_planet
	}
	return 0.0
}