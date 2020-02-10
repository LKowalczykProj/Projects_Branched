import random
from .constants import Constants
from .enums import *


class Expert:

    def __init__(self, actors):
        self.Actors = actors
        self.questions = []
        for param in Constants.expert_questions:
            self.questions.append(param)
        self.current_question = None
        self.current_parameter = None
        self.last_string_index = 6
        self.last_enum_index = 10
        self.dataset = {}

    def random_answer(self):
        total = self.Actors.count()
        rand = random.randint(0, total - 1)
        print(rand)
        guess = self.Actors[rand]
        self.Actors = self.Actors.exclude(id=guess.id)
        print(self.Actors)
        return guess

    def restart(self,fresh_batch):
        self.Actors = fresh_batch
        self.questions = []
        for q in Constants.expert_question_names:
            self.questions.append(q)

    def ask_question(self):
        print("*"+self.current_question)
        print(self.questions)
        self.questions.remove(self.current_question)
        if self.current_question == Constants.expert_question_names[0]:
            dict = {}
            for obj in self.Actors:
                letter = obj.firstname[0]
                if letter in dict:
                    dict[letter] += 1
                else:
                    dict[letter] = 1
            max = -1
            key = -1
            for k in dict.keys():
                if dict[k] > max:
                    key = k
            self.current_parameter = key
            return Constants.expert_questions[self.current_question].format(key)
        elif self.current_question == Constants.expert_question_names[1]:
            dict = {}
            for obj in self.Actors:
                letter = obj.firstname[-1]
                if letter in dict:
                    dict[letter] += 1
                else:
                    dict[letter] = 1
            max = -1
            key = -1
            for k in dict.keys():
                if dict[k] > max:
                    key = k
            self.current_parameter = key
            return Constants.expert_questions[self.current_question].format(key)
        elif self.current_question == Constants.expert_question_names[2]:
            dict = {}
            for obj in self.Actors:
                letter = obj.lastname[0]
                if letter in dict:
                    dict[letter] += 1
                else:
                    dict[letter] = 1
            max = -1
            key = -1
            for k in dict.keys():
                if dict[k] > max:
                    key = k
            self.current_parameter = key
            return Constants.expert_questions[self.current_question].format(key)
        elif self.current_question == Constants.expert_question_names[3]:
            dict = {}
            for obj in self.Actors:
                letter = obj.lastname[-1]
                if letter in dict:
                    dict[letter] += 1
                else:
                    dict[letter] = 1
            max = -1
            key = -1
            for k in dict.keys():
                if dict[k] > max:
                    key = k.upper()
            self.current_parameter = key
            return Constants.expert_questions[self.current_question].format(key)
        elif self.current_question == Constants.expert_question_names[4]:
            age_list = []
            for obj in self.Actors:
                age_list.append(Constants.expert_current_year-obj.birth_year)
            age_list.sort()
            median = age_list[int(len(age_list)/2)]
            self.current_parameter = median
            return Constants.expert_questions[self.current_question].format(median)
        elif self.current_question == Constants.expert_question_names[5]:
            age_list = []
            for obj in self.Actors:
                age_list.append(Constants.expert_current_year-obj.birth_year)
            age_list.sort()
            median = age_list[int(len(age_list)/2)]
            self.current_parameter = median
            return Constants.expert_questions[self.current_question].format(median)
        elif Constants.expert_question_names.index(self.current_question) < self.last_enum_index:
            return Constants.expert_questions[self.current_question].format(self.current_parameter)
        else:
            return Constants.expert_questions[self.current_question]

    def count(self, key):
        if key == Constants.expert_question_names[6]:
            male = self.Actors.filter(gender=Gender.Male).count()
            female = self.Actors.filter(gender=Gender.Female).count()
            maximum = max(male, female)
            if male == maximum:
                return [maximum, Gender.Male]
            else:
                return [maximum, Gender.Female]
        elif key == Constants.expert_question_names[7]:
            blond = self.Actors.filter(hair_color=HairColor.Blond).count()
            black = self.Actors.filter(hair_color=HairColor.Black).count()
            brown = self.Actors.filter(hair_color=HairColor.Brown).count()
            red = self.Actors.filter(hair_color=HairColor.Red).count()
            maximum = max(blond, black, brown, red)
            if blond == maximum:
                return [maximum, HairColor.Blond]
            if brown == maximum:
                return [maximum, HairColor.Brown]
            if black == maximum:
                return [maximum, HairColor.Black]
            if red == maximum:
                return [maximum, HairColor.Red]
        elif key == Constants.expert_question_names[8]:
            white = self.Actors.filter(skin_color=Ethnicity.White).count()
            black = self.Actors.filter(skin_color=Ethnicity.Black).count()
            yellow = self.Actors.filter(skin_color=Ethnicity.Yellow).count()
            brown = self.Actors.filter(skin_color=Ethnicity.Brown).count()
            maximum = max(white, black, yellow, brown)
            if white == maximum:
                return [maximum, Ethnicity.White]
            if black == maximum:
                return [maximum, Ethnicity.Black]
            if yellow == maximum:
                return [maximum, Ethnicity.Yellow]
            if brown == maximum:
                return [maximum, Ethnicity.Brown]
        elif key == Constants.expert_question_names[9]:
            usa = self.Actors.filter(country=Country.USA).count()
            canada = self.Actors.filter(country=Country.Canada).count()
            china = self.Actors.filter(country=Country.China).count()
            england = self.Actors.filter(country=Country.Australia).count()
            other = self.Actors.filter(country=Country.Europe).count()
            maximum = max(usa, canada, china, england, other)
            if usa == maximum:
                return [maximum, Country.USA]
            if canada == maximum:
                return [maximum, Country.Canada]
            if china == maximum:
                return [maximum, Country.China]
            if england == maximum:
                return [maximum, Country.Australia]
            if other == maximum:
                return [maximum, Country.Europe]
        else:
            positive = self.Actors.filter(**{key: True}).count()
            negative = self.Actors.filter(**{key: False}).count()
            if positive < negative:
                return [negative, "false"]
            else:
                return [positive, "true"]

    def query(self):
        if self.Actors.count() == 0:
            return Constants.expert_empty
        if self.Actors.count() == 1:
            return Constants.expert_end
        else:
            if len(self.questions) == 0:
                return Constants.expert_unknown
            elif len(self.questions) <= self.last_string_index:
                rand = random.randint(0, len(self.questions) - 1)
                self.current_question = self.questions[rand]
                return self.ask_question()
            else:
                lowest_maximum = 999999999
                for question in self.questions[self.last_string_index:]:
                    temp_max = self.count(question)
                    print("{0} -> {1}".format(temp_max,question))
                    if temp_max[0] < lowest_maximum:
                        self.current_parameter = temp_max[1]
                        self.current_question = question
                        lowest_maximum = temp_max[0]
                return self.ask_question()

    def update(self, answer):
        if answer == Constants.expert_answer_confirm:
            if self.current_question == Constants.expert_question_names[0]:
                self.Actors = self.Actors.filter(firstname__startswith=self.current_parameter)
            elif self.current_question == Constants.expert_question_names[1]:
                self.Actors = self.Actors.filter(firstname__endswith=self.current_parameter)
            elif self.current_question == Constants.expert_question_names[2]:
                self.Actors = self.Actors.filter(lastname__startswith=self.current_parameter)
            elif self.current_question == Constants.expert_question_names[3]:
                self.Actors = self.Actors.filter(lastname__endswith=self.current_parameter)
            elif self.current_question == Constants.expert_question_names[4]:
                self.Actors = self.Actors.filter(birth_year__gt=int(self.current_parameter))
            elif self.current_question == Constants.expert_question_names[5]:
                self.Actors = self.Actors.filter(birth_year__lte=int(self.current_parameter))
            elif Constants.expert_question_names.index(self.current_question) < self.last_enum_index:
                self.Actors = self.Actors.filter(**{self.current_question: self.current_parameter})
            else:
                self.Actors = self.Actors.filter(**{self.current_question: bool(self.current_parameter)})
        if answer == Constants.expert_answer_reject:
            if self.current_question == Constants.expert_question_names[0]:
                self.Actors = self.Actors.exclude(firstname__startswith=self.current_parameter)
            elif self.current_question == Constants.expert_question_names[1]:
                self.Actors = self.Actors.exclude(firstname__endswith=self.current_parameter)
            elif self.current_question == Constants.expert_question_names[2]:
                self.Actors = self.Actors.exclude(lastname__startswith=self.current_parameter)
            elif self.current_question == Constants.expert_question_names[3]:
                self.Actors = self.Actors.exclude(lastname__endswith=self.current_parameter)
            elif self.current_question == Constants.expert_question_names[4]:
                self.Actors = self.Actors.filter(birth_year__lt=int(self.current_parameter))
            elif self.current_question == Constants.expert_question_names[5]:
                self.Actors = self.Actors.filter(birth_year__gte=int(self.current_parameter))
            elif Constants.expert_question_names.index(self.current_question) < self.last_enum_index:
                self.Actors = self.Actors.exclude(**{self.current_question: self.current_parameter})
            else:
                self.Actors = self.Actors.exclude(**{self.current_question: bool(self.current_parameter)})
        print(self.Actors)
        return "ignore"

    def get_answer(self):
        return self.Actors[0]

    def get_dataset(self):
        return self.dataset
