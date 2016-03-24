from flask import *

api = Blueprint('api', __name__, template_folder = 'views')

@api.route('/api/search', methods = ['GET'])
def searchViewTable(query):
	return True

"""var newTrip = Trip(filename: "t1",
            name: "Bird Hills Nature Area",
            address: "Newport Road, Ann Arbor MI",
            distance: 4.6,
            length: 8,
            duration: 3,
            level: 1,
            timings: "6AM - 10PM, Everyday",
            temp: 66, //why?
            weather: "Cloudy", //what is this for?
            shelter: ["no facilities"],
            equipment: ["water"],
            clothes: ["dress appropriately for weather"],
            food: ["water"], //what is this for?
            season: [Season.ANY],
            description: "Bird Hills Nature Area is the largest park in the city. Its hilly woods are a sanctuary for hikers. The area is closed to bicycles to prevent damage from erosion. The park is bordered by Newport Rd on the west, Bird Rd on the north, Huron River Dr on the east and M-14 on the south. A parking lot is located on Newport Rd. A small pull-off parking area is located on Bird Rd. Parking is also available in the Barton Nature Area lot, near the Barton Dam. There are five trailheads: at Down Up Circle, at Bird Rd, at Beechwood Dr, and two near the Newport Rd parking area.")
        //no bikes allowed, good for dogs
        allTripList.append(newTrip)

        newTrip = Trip(filename: "tunip-rock",
            name: "Turnip Rock - Pointe aux Barques trail",
            address: "Gill Road, Port Austin, MI",
            distance: 157,
            length: 7,
            duration: 3,
            level: 2,
            timings: "7AM - 4PM, Sat-Sun", //couldn't find
            temp: 64,
            weather: "Cloudy",
            shelter: ["no shelter"],
            equipment: ["water"],
            clothes: ["kayak ready"],
            food: ["2 Gal water"],
            season: [Season.ANY],
            description: "Turnip Rock is a small geological formation in Michigan. It is located in Lake Huron, in shallow water a few meters offshore, near the rock called the Thumbnail. Turnip Rock has been severely undercut by wave action, so that its top has a significantly larger cross-section than its base. Its consequent unusual form, reminiscent of a turnip, has made it a minor attraction for viewing from watercraft, although it is privately owned and not open to the public. Port Austin, the nearest large community, is the usual base for kayaking trips to Turnip Rock. A concrete collar has been built around the base of Turnip Rock at the waterline to slow further undercutting. Turnip Rock was one of twenty finalists in the 2013 'Seven Wonders of Michigan' contest sponsored by the Detroit Free Press and the Lansing State Journal, but wasn't selected as one of the final seven")
        //kayak to the rock, private property
        allTripList.append(newTrip)

        newTrip = Trip(filename: "t3",
            name: "Lakelands Trail",
            address: "Hamburg Road, Pinckney MI",
            distance: 24.8,
            length: 7,
            duration: 4,
            level: 1,
            timings: "7AM - 4PM, Sat-Sun", //N/A?
            temp: 62,
            weather: "Cloudy",
            shelter: ["equestrian campgrounds"],
            equipment: ["riding items if you bring your horse"],
            clothes: ["riding attire"],
            food: ["water"],
            season: [Season.ANY],
            description: "Lakelands Trail State Park is a state park in Michigan that runs east-west from Stockbridge to Hamburg Township, Michigan. It is a multi-use trail converted from abandoned railroad corridors. The north side of the trail is for hiking and biking, and the south side is for horseback riding. The surface from Stockbridge to Pinckney is composed of crushed limestone. 6 miles are paved in Hamburg Township. From Stockbridge to Pinckney, horses are routinely ridden on the unpaved trail surface. Only the paved portion from just west of Pinckney to the east end in Hamburg Township is consistently usable by bicyclists.")
        //multiple trailheads - https://en.wikipedia.org/wiki/Lakelands_Trail_State_Park
        //horseback riding
        allTripList.append(newTrip)

        newTrip = Trip(filename: "t4",
            name: "Maybury State Park",
            address: "Maybury-Hiking Trail",
            distance: 3,
            length: 6,
            duration: 2.5,
            level: 1,
            timings: "8AM - 10PM, Sun-Sat",
            temp: 52,
            weather: "Partly Cloudy",
            shelter: ["picnic area", "picnic shelter", "group use area"],
            equipment: ["backpack", "recreation passport"],
            clothes: ["hiking boots"],
            food: ["bottled water", "snacks"],
            season: [Season.ANY],
            description: "Six miles of unpaved hiking trails meander through wooded areas and around a large pond at Maybury State Park")
        allTripList.append(newTrip)

        newTrip = Trip(filename: "t5",
            name: "Mackinac Island",
            address: "Round the Shore",
            distance: 250,
            length: 8.2,
            duration: 3,
            level: 1,
            timings: "8AM - 8AM, Sun-Sat",
            temp: 45,
            weather: "Sunny",
            shelter: ["restaurants", "shops"],
            equipment: ["none"],
            clothes: ["comfortable clothes"],
            food: ["bottled water", "snacks"],
            season: [Season.ANY],
            description: "Most of Mackinac Island is state park, circled and crisscrossed by a skein of trails.")
        allTripList.append(newTrip)

        newTrip = Trip(filename: "t6",
            name: "Dolph Park Nature Area",
            address: "Jackson Road",
            distance: 3,
            length: 0.5,
            duration: 0.25,
            level: 1,
            timings: "8AM - 10PM, Sun-Sat",
            temp: 54,
            weather: "Partly Cloudly",
            shelter: ["none"],
            equipment: ["backpack"],
            clothes: ["hiking boots"],
            food: ["bottled water", "snacks"],
            season: [Season.SUMMER, Season.FALL, Season.WINTER],
            description: "Dolph Park Nature Area is a 0.5 mile loop trail located near Ann Arbor, Michigan and is good for all skill levels. The trail is primarily used for hiking and is accessible from March until January.")
        allTripList.append(newTrip)

        newTrip = Trip(filename: "t7",
            name: "Robert & Nancy Smith Trail",
            address: "Bent Tree Drive",
            distance: 10.4,
            length: 1.5,
            duration: 1,
            level: 3,
            timings: "7AM - 4PM, Sat-Sun",
            temp: 27,
            weather: "Cloudy",
            shelter: ["campground", "lodge"],
            equipment: ["backpack"],
            clothes: ["boots", "jacket"],
            food: ["protein bars", "water"],
            season: [Season.ANY],
            description: "Great trail to train on or just have fun.")
        allTripList.append(newTrip)

        newTrip = Trip(filename: "t8",
            name: "Hudson Mills Metropark",
            address: "North Territorial Road",
            distance: 11.5,
            length: 12,
            duration: 6,
            level: 1,
            timings: "7AM - 4PM, Sat-Sun",
            temp: 27,
            weather: "Cloudy",
            shelter: ["campground", "lodge"],
            equipment: ["backpack", "flashlight"],
            clothes: ["snow boots"],
            food: ["1Gal water"],
            season: [Season.ANY],
            description: "Hudson Mills metropark is a 9 mile point-to-point trail located near Dexter Twp, MI that features a river and is good for all skill levels. The trail is primarily used for hiking, walking, and road biking and is accessible from March until October. Dogs are also able to use this trail but must be kept on leash.")
        allTripList.append(newTrip)

        newTrip = Trip(filename: "t9",
            name: "Potawatomi Trail",
            address: "Glenbrook Road",
            distance: 19.7,
            length: 14,
            duration: 7,
            level: 2,
            timings: "7AM - 4PM, Sat-Sun",
            temp: 27,
            weather: "Cloudy",
            shelter: ["campground", "lodge"],
            equipment: ["backpack", "flashlight"],
            clothes: ["snow boots"],
            food: ["1Gal water"],
            season: [Season.ANY],
            description: "Potawatomi Trail is a 12.7 mile loop trail located near Unadilla Township, MI that features a lake and is rated as difficult. The trail offers a number of activity options and is accessible from March until November. Dogs are also able to use this trail but must be kept on leash.")
        allTripList.append(newTrip)

        newTrip = Trip(filename: "indep",
            name: "Independence Lake Trail Loop",
            address: "Sashabaw Road",
            distance: 23,
            length: 1.7,
            duration: 1,
            level: 1,
            timings: "10AM - 5PM, Fri-Sun",
            temp: 48,
            weather: "Cloudy",
            shelter: ["Nature Center", "lodge"],
            equipment: ["backpack", "flashlight", "trekking pole"],
            clothes: ["running shoes", "fleece jacket"],
            food: ["protein bars", "1Gal water"],
            season: [Season.ANY],
            description: "Independence lake trail loop is a 1.7 mile loop trail located near Webster Twp, Michigan that features a lake and is good for all skill levels. The trail offers a number of activity options and is accessible year-round. Dogs are also able to use this trail but must be kept on leash.")
        allTripList.append(newTrip)


        newTrip = Trip(filename: "pictured",
            name: "Pictured Rocks Lakeshore",
            address: "Munising",
            distance: 24,
            length: 20,
            duration: 10,
            level: 3,
            timings: "9AM - 4:30PM, Sat-Sun",
            temp: 36,
            weather: "Cloudy",
            shelter: ["campground", "lodge"],
            equipment: ["backpack", "flashlight", "trekking pole"],
            clothes: ["snow boots", "down jacket"],
            food: ["protein bars", "1Gal water"],
            season: [Season.ANY],
            description: "Sandstone cliffs, beaches, sand dunes, waterfalls, lakes, forest, and shoreline beckon you to visit Pictured Rocks National Lakeshore. Hiking, camping, sightseeing, and four season outdoor opportunities abound. The lakeshore hugs the Lake Superior shoreline for more than 40 miles. Lake Superior is the largest, deepest, coldest, and most pristine of all the Great Lakes.")
        allTripList.append(newTrip)


        newTrip = Trip(filename: "isle",
            name: "Isle Royale National Park",
            address: "Houghton Township",
            distance: 24,
            length: 20,
            duration: 11,
            level: 3,
            timings: "7AM - 4PM, All days",
            temp: 34,
            weather: "Cloudy",
            shelter: ["Rock Harbor lodge"],
            equipment: ["backpack", "flashlight", "trekking pole"],
            clothes: ["snow boots", "down jacket"],
            food: ["protein bars", "1Gal water"],
            season: [Season.ANY],
            description: "Explore a rugged, isolated island, far from the sights and sounds of civilization. Surrounded by Lake Superior, Isle Royale offers unparalleled solitude and adventures for backpackers, hikers, boaters, kayakers, canoeists and scuba divers. Here, amid stunning scenic beauty, you'll find opportunities for reflection and discovery, and make memories that last a lifetime.")
        allTripList.append(newTrip)"""
